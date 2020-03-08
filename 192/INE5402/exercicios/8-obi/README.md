**Os índices das questões são clicáveis e levam à resolução do exercício.**

[1.](1.py) No mundo da matemática, para sabermos se um grande número é divisível por outro existe uma regra, chamada de regra de divisibilidade. Um número natural é divisível por 3 quando a soma de todos os seus algarismos forma um número divisível por 3, ou seja, um múltiplo de 3.
    Ex1: 1.104 é divisível por 3?
        SIM. É divisível por 3, pois seus algarismos quando somados: 1 + 1 + 0 + 4 = 6, que é um número divisível por 3 (porque 6 ÷ 3 = 2, que é um número natural).
    Ex2: 2.791.035 é divisível por 3?
        SIM. 2.791.035 é constituído de algarismos que somados: 2 + 7 + 9 + 1 + 0 + 3 + 5 = 27, gera um número divisível por 3 (pois 27 ÷ 3 = 9, número natural).
    Entrada:
        O arquivo de entrada conterá dois números, n (1< n <10) indicando o número de algarismos de m, (1< m < 1000000000). A entrada termina com o fim do arquivo (EOF).
    
    Saída:
        Seu programa deve fornecer o número da soma dos algarismos de m e logo depois apresentar “sim” caso o número seja divisível por 3 ou “não” caso não seja. 


[2.](2.py) Dona Parcinova, mãe de Mangojata, pediu a ela que ajudasse a calcular o consumo de frutas da casa e a quantidade gasta por dia nestas frutas. Mangojata agora deve então fazer um programa a partir de uma tabela que sua mãe estava utilizando para anotações há quase um ano. Nesta tabela, dona Parcinova anotou a quantidade de dias e depois o valor gasto cada dia e as frutas compradas naquele dia, sempre na quantidade de um KG por tipo de fruta.
    Entrada:
        A primeira linha de entrada contém um inteiro N (1 ≤ N ≤ 365) que indica o número de casos de teste que vem a seguir. Cada caso de teste é composto por 2 linhas. A primeira linha contém um valor de ponto flutuante V (0.10 ≤ V ≤ 20.00) indicando o valor gasto no dia e a segunda linha contém o nome de cada uma das frutas que dona Parcinova comprou.
    
    Saída:
        Para cada caso de teste, imprima quantos kg de frutas dona Parcinova comprou em cada dia, com mensagem correspondente em inglês, conforme exemplo abaixo. No final, apresente o consumo médio em kg por dia com 2 casas decimais seguido da mensagem correspondente e a média de gasto por dia com as frutas, também em inglês e com mensagem correspondente, conforme o exemplo abaixo.
    Obs.: Todas as letras da saída devem ser impressas em minúsculas, com exceção do "R" de "R$"


[3.](3.py) Preencher formulários é uma tarefa simples. Mas é preciso conferir se o espaço reservado para os dados é suficiente. Sua tarefa é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres.
    Entrada:
        A entrada é uma linha de texto L (1 ≤ |L| ≤ 500).
    
    Saída: A saída é dada em uma única linha. Ela deve ser "YES" (sem as aspas) se a linha de texto L tem até 80 caracteres. Se L tem mais de 80 caracteres, a saída deve ser "NO".


[4.](4.py) Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las, alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira letra da segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada.
    Entrada:
        A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste que vem a seguir. Cada caso de teste é composto por uma linha que contém duas cadeias de caracteres, cada cadeia de caracteres contém entre 1 e 50 caracteres inclusive.
    
    Saída:
        Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a cadeia resultante.


[5.](5.py) O professor João decidiu aplicar somente provas de múltipla escolha, para facilitar a correção. Em cada prova, cada questão terá cinco alternativas (A, B, C, D e E), e o professor vai distribuir uma folha de resposta para cada aluno. Ao final da prova, as folhas de resposta serão escaneadas e processadas digitalmente para se obter a nota de cada aluno.

Inicialmente, ele pediu ajuda a um sobrinho, que sabe programar muito bem, para escrever um programa para extrair as alternativas marcadas pelos alunos nas folhas de resposta. O sobrinho escreveu uma boa parte do software, mas não pode terminá-lo, pois precisava treinar para a Maratona de Programação.

Durante o processamento, a prova é escaneada usando tons de cinza entre 0 (preto total) e 255 (branco total). Após detectar os cinco retângulos correspondentes a cada uma das alternativas, ele calcula a média dos tons de cinza de cada pixel, retornando um valor inteiro correspondente àquela alternativa. Se o quadrado foi preenchido corretamente o valor da média é zero (preto total). Se o quadrado foi deixado em branco o valor da média é 255 (branco total). Assim, idealmente, se os valores de cada quadrado de uma questão são (255, 0, 255, 255, 255), sabemos que o aluno marcou a alternativa B para essa questão. No entanto, como as folhas são processadas individualmente, o valor médio de nível de cinza para o quadrado totalmente preenchido não é necessariamente 0 (pode ser maior); da mesma forma, o valor para o quadrado não preenchido não é necessariamente 255 (pode ser menor). O prof. João determinou que os quadrados seriam divididos em duas classes: aqueles com média menor ou igual a 127 serão considerados pretos e aqueles com média maior a 127 serão considerados brancos.

Obviamente, nem todas as questões das folhas de resposta são marcadas de maneira correta. Pode acontecer de um aluno se enganar e marcar mais de uma alternativa na mesma questão, ou não marcar nenhuma alternativa. Nesses casos, a resposta deve ser desconsiderada.

O professor João necessita agora de um voluntário para escrever um programa que, dados  os valores dos cinco retângulos correspondentes às alternativas de uma questão determine qual a alternativa corretamente marcada, ou se a resposta à questão deve ser desconsiderada.

    Entrada:
        A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um número inteiro N indicando o número de questões da folha de respostas (1 ≤ N ≤ 255). Cada uma das N linhas seguintes descreve a resposta a uma questão e contém cinco números inteiros A, B, C, D e E, indicando os valores de nível de cinza médio para cada uma das alternativas da resposta (0 ≤ A, B, C, D, E ≤ 255). O último caso de teste é seguido por uma linha que contém apenas um número zero.
    
    Saída: 
        Para cada caso de teste da entrada seu programa deve imprimir N linhas, cada linha correspondendo a uma questão. Se a resposta à questão foi corretamente preenchida na folha de resposta, a linha deve conter a alternativa marcada (‘A’, ‘B’, ‘C’, ‘D’ ou ‘E’). Caso contrário, a linha deve conter o caractere ‘*’ (asterisco).