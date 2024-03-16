import * as esbuild from 'esbuild'
import { glob } from 'glob'

// Note: esbuild plugin glob not available yet for esbuild 0.17+.
//  This workaround won't scan for new files while watching.
// ref: https://github.com/waspeer/esbuild-plugin-glob
const entryPoints = await glob('src/**/solution.{ts,js}')
console.log('entryPoints:')
entryPoints?.forEach(entry => console.log(entry))

let ctx = await esbuild.context({
  entryPoints,
  bundle: true,
  write: true,
  outdir: 'dist',
  target: 'ESNext',
  sourcemap: true,
  format: 'esm',
  minify: false,
  platform: 'node',
})

await ctx.watch()
console.log('esbuild watching...')