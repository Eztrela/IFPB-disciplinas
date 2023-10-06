export class Livro {

    constructor(public titulo:string = '',
                public edicao: number,
                public isbn: string = '',
                public autores: Array<string> = []) {
    }
  }