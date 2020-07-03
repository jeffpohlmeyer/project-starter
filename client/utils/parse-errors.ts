import upperFirst from 'lodash.upperfirst'
import toLower from 'lodash.tolower'

interface ErrorInterface {
  [key: string]: string[]
}

export default function useErrorParser(errors: ErrorInterface): string {
  let message = ''
  Object.values(errors).forEach((v) => {
    v.forEach((error) => {
      message += `${upperFirst(toLower(error))}  `
    })
  })

  return message
}
