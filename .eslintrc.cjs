module.exports = {
  root: true,
  extends: [
    //
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
  ],
  env: {
    node: true,
    es6: true,
  },
  parser: '@typescript-eslint/parser',
  plugins: [
    //
    '@typescript-eslint',
  ],
  parserOptions: {
    project: [
      //
      './tsconfig.json',
    ],
    ecmaVersion: "latest",
    sourceType: "module",
  },
  overrides: [
    {
      files: ["**/__tests__/**/*"],
      env: {
        jest: true,
      },
    },
  ],
}
