const fs = require('fs');

// open profile.json and parse it
// return the parsed object
function parse() {
  const prof = JSON.parse(fs.readFileSync('./profile.json'));
  // Compute overall usage.
  let cpu_python = 0;
  let cpu_native = 0;
  let cpu_system = 0;
  let mem_python = 0;
  let mem_native = 0;
  let max_alloc = 0;
  let cp = {};
  let cn = {};
  let cs = {};
  let mp = {};
  let ma = {};
  for (const f in prof.files) {
    cp[f] = 0;
    cn[f] = 0;
    cs[f] = 0;
    mp[f] = 0;
    ma[f] = 0;
    for (const l in prof.files[f].lines) {
      const line = prof.files[f].lines[l];
      cp[f] += line.n_cpu_percent_python;
      cn[f] += line.n_cpu_percent_c;
      cs[f] += line.n_sys_percent;
      if (line.n_peak_mb > ma[f]) {
        ma[f] = line.n_peak_mb;
        mp[f] += line.n_peak_mb * line.n_python_fraction;
      }
      max_alloc += line.n_malloc_mb;
    }
    cpu_python += cp[f];
    cpu_native += cn[f];
    cpu_system += cs[f];
    mem_python += mp[f];
  }
  if (prof.memory) {
    const mem = prof.max_footprint_mb;
    const py_mem = (mem_python / max_alloc) * prof.max_footprint_mb;
    const native_mem = mem - py_mem;

    console.log(
      `${mem.toFixed(2)},${py_mem.toFixed(2)},${native_mem.toFixed(2)}`
    );
  }
}

parse();
