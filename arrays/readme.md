## Структуры данных

- ### Массивы
    - Реализация динамического вектора.
    - [ ] Описание:
        - [Массивы (видео)](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)
        - [UCBerkley CS61B - Линейные и многомерные массивы (видео)](https://youtu.be/Wp8oiO_CZZE?t=15m32s)
        - [Основные массивы (видео)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Basic-arrays/149042/177104-4.html)
        - [Многомерные массивы (видео)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Multidimensional-arrays/149042/177105-4.html)
        - [Динамические массивы (видео)](https://www.coursera.org/learn/data-structures/lecture/EwbnV/dynamic-arrays)
        - [Массив массивов (видео)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
        - [Массив массивов (видео)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Jagged-arrays/149042/177106-4.html)
        - [Динамические массивы (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Resizable-arrays/149042/177108-4.html)
    - [ ] Реализация вектора (изменяемый массив с автоматическим изменением размера):
        - [ ] Тренируйтесь программировать используя массивы, указатели и арифметику указателей для перехода к индексу вместо индексации.
        - [ ] выделение памяти для массива
            - можно выделить память для массива целых чисел, просто не используя его возможности
            - начиная с 16, или если начальная цифра больше, использовать степень 2 - 16, 32, 64, 128
        - [ ] size() - количество элементов
        - [ ] capacity() - количество элементов которое он может содержать
        - [ ] is_empty()
        - [ ] at(index) - возвращает элемент по индексу
        - [ ] push(item)
        - [ ] insert(index, item) - вставка элемента по индексу, сдвигает значение по индексу и следующие за ним элементы вправо
        - [ ] prepend(item) - может вставить элемент выше индекса 0
        - [ ] pop() - удалить последний элемент, вернуть значение
        - [ ] delete(index) - удаляет элемент по индексу, сдвигает все следующие за ним элементы влево
        - [ ] remove(item) - ищет элементы по значению и удаляет их, даже если их несколько
        - [ ] find(item) - ищет элемент по значению и возвращает индекс первого найденного элемента, возвращает -1 если ничего не найдено
        - [ ] resize(new_capacity) // private function
            - когда массив полностью заполнен, увеличивает его размер вдвое
            - при добавлении элемента, если размер массива 1/4 от общего размера, увеличиваем на половину
    - [ ] Время
        - O(1) для операций add/remove в конце (амортизируется для размещения большего объема), index, или update
        - O(n) для insert/remove в любом месте
    - [ ] Работа с памятью
        - смежные в памяти, это помогает повысить производительность
        - необходимое пространство = (размер массива, который >= n) * размер элемента, но даже если 2n, по прежнему O(n)

- ### Связные списки (Linked Lists)
    - [ ] Описание:
        - [ ] [Singly Linked Lists (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
        - [ ] [CS 61B - Linked Lists (video)](https://www.youtube.com/watch?v=sJtJOtXCW_M&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd&index=5)
    - [ ] [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo)
            - не все видео целиком, только кусочки об узлах и распределении памяти.
    - [ ] Связные списки vs Массивы:
        - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays)
        - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays)
    - [ ] [why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
    - [ ] Ага, попался: тебе нужны знания указателей на указатели:
        (для тех случаев, когда ты передаешь указатель функции, которая может менять адрес, куда указывает указатель)
        Это страница просто для того, чтобы понять указатели на указатели. Читабельность и обслуживаемость страдает 
        из-за искусности.
        - [Указатели на указатели](https://www.eskimo.com/~scs/cclass/int/sx8.html)
    - [ ] воплотить в жизнь (я сделал это с помощью указателя на хвост и без): 
        - [ ] size() - возвращает количество элементов в листе
        - [ ] empty() - возвращет true если список пуст
        - [ ] value_at(n) - возращет значение n-го элемента, где 0 - первый элемент
        - [ ] push_front(value) - добавляет элемент в начало списка
        - [ ] pop_front() - удаляет первый и возращает его значение
        - [ ] push_back(value) - добавляет элемент в конец списка
        - [ ] pop_back() - удаляет последний и возращает его значение
        - [ ] front() - возращает значение первого элемента в списке
        - [ ] back() - возращает значение последнего элемента в списке
        - [ ] insert(index, value) - помещает значение (value) в элемент по индексу (index), при этом заменяемый элемент
        добавлен в список как новый элемент
        - [ ] erase(index) - удаляет узел (элемент) по данному индексу
        - [ ] value_n_from_end(n) - возращает значение n-го элемента c конца списка
        - [ ] reverse() - реверсирует весь список
        - [ ] remove_value(value) - удаляет первый элемент в списке с указанным значением (value)
    - [ ] Двусвязный список
        - [Описание (video)](https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists)
        - Можно не делать

- ### Стек
    - [ ] [Стек (video)](https://www.coursera.org/learn/data-structures/lecture/UdKzQ/stacks)
    - [ ] [Использование стека Last-In First-Out (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Using-stacks-last-first-out/149042/177120-4.html)
    - [ ] Не будет реализован. Реализация с помощью массива очевидна.

- ### Очередь
    - [ ] [Использование очереди First-In First-Out(video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Using-queues-first-first-out/149042/177122-4.html)
    - [ ] [Очередь (video)](https://www.coursera.org/learn/data-structures/lecture/EShpq/queue)
    - [ ] [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
    - [ ] [Очередь с приоритетом (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Priority-queues-deques/149042/177123-4.html)
    - [ ] Реализация с использованием связанного списка и указателя на последний элемент(tail):
        - enqueue(value) - добавляет элемент в конец очереди
        - dequeue() - возвращает значение и удаляет из очереди последний добавленный элемент(front)
        - empty()
    - [ ] Реализация с применением массива фиксированного размера:
        - enqueue(value) - добавляет элемент в конец очереди
        - dequeue() - возвращает значение и удаляет из очереди последний добавленный элемент
        - empty()
        - full()
    - [ ] Затраты:
        - плохая реализация с применением связанного списка когда элемент добавляется в начало очереди и удаляется с конца очереди за O(n),
          операция dequeue в таком случае будет требовать каждый раз обхода всего списка
        - enqueue: O(1) (amortized, связанный список и массив [probing])
        - dequeue: O(1) (связанный список и массив)
        - empty: O(1) (связанный список и массив)

- ### Хеш-таблица
    - [ ] Видео:
        - [ ] [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
        - [ ] [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [ ] [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [ ] [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
        - [ ] [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
        - [ ] [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)

    - [ ] Онлайн курсы:
        - [ ] [Understanding Hash Functions (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Understanding-hash-functions/149042/177126-4.html)
        - [ ] [Using Hash Tables (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Using-hash-tables/149042/177127-4.html)
        - [ ] [Supporting Hashing (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Supporting-hashing/149042/177128-4.html)
        - [ ] [Language Support Hash Tables (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Language-support-hash-tables/149042/177129-4.html)
        - [ ] [Core Hash Tables (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/m7UuP/core-hash-tables)
        - [ ] [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/3)
        - [ ] [Phone Book Problem (video)](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)
        - [ ] распределенные хеш-таблицы:
            - [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/learn/data-structures/lecture/DvaIb/instant-uploads-and-storage-optimization-in-dropbox)
            - [Distributed Hash Tables (video)](https://www.coursera.org/learn/data-structures/lecture/tvH8H/distributed-hash-tables)

    - [ ] реализация с помощью массива и применением linear probing
        - hash(k, m) - m размер хеш-таблицы
        - add(key, value) - если ключ уже существует обновляем значение
        - exists(key)
        - get(key)
        - remove(key)

## Дополнительно

- ### Бинарный поиск
    - [ ] [Бинарный поиск (видео на ютубе)](https://www.youtube.com/watch?v=D5SrAga1pno)
    - [ ] [Бинарный поиск (видео на khanacademy)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
    - [ ] [Длинная статья с деталями](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/)
    - [ ] Реализация:
        - бинарный поиск (на отсортированном числовом массиве)
        - бинарный поиск с использованием рекурсии

- ### Побитовые операции
    - [ ] [Bits cheat sheet](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf) - ты должен знать сколько степеней двойки от (2^1 до 2^16 и 2^32)
    - [ ] Даст отличное понимание манипуляций битами с помощью: &, |, ^, ~, >>, <<
        - [ ] [words](https://en.wikipedia.org/wiki/Word_(computer_architecture))
        - [ ] Хорошее введение:
            [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
        - [ ] [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
        - [ ] [Bit Manipulation](https://en.wikipedia.org/wiki/Bit_manipulation)
        - [ ] [Bitwise Operation](https://en.wikipedia.org/wiki/Bitwise_operation)
        - [ ] [Bithacks](https://graphics.stanford.edu/~seander/bithacks.html)
        - [ ] [The Bit Twiddler](http://bits.stephan-brumme.com/)
        - [ ] [The Bit Twiddler Interactive](http://bits.stephan-brumme.com/interactive.html)
    - [ ] 2s и 1s дополнения:
        - [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
        - [1s Complement](https://en.wikipedia.org/wiki/Ones%27_complement)
        - [2s Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
    - [ ] счетчик битов:
        - [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
        - [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
        - [How To Count The Number Of Set Bits In a 32 Bit Integer](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer)
    - [ ] округление до следующей степени 2:
        - [Round Up To Next Power Of Two](http://bits.stephan-brumme.com/roundUpToNextPowerOfTwo.html)
    - [ ] обмен значениями:
        - [Swap](http://bits.stephan-brumme.com/swap.html)
    - [ ] абсолютные значения:
        - [Absolute Integer](http://bits.stephan-brumme.com/absInteger.html)

## Деревья

- ### Деревья, Заметки и Основные понятия
    - [ ] [Основы деревьев (видео)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
    - [ ] [Деревья (видео)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
    - базовые конструкции деревьев
    - обход
    - алгоритмы манипуляции
    - BFS (breadth-first search - поиск в ширину)
        - [MIT (видео)](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
        - порядок уровня (BFS, использование очереди)
            сложность по времени выполнения: O(n)
            сложность по памяти: лучшая: O(1), худшая: O(n/2)=O(n)
    - DFS (depth-first search - поиск в глубину)
        - [MIT (видео)](https://www.youtube.com/watch?v=AfSk24UTFS8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=14)
        - заметки:
            сложность по времени выполнения: O(n)
            сложность по памяти:
                лучшая: O(log n) - средняя высота дерева
                худшая: O(n)
        - in-order (DFS: левый, вершина, правый)
        - post-order (DFS: левый, правый, вершина)
        - pre-order (DFS: вершина, левый, правый)

- ### Бинарное дерево поиска (BST: Binary search trees)
    - [ ] [Обзор бинарного дерева поиска (видео)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
    - [ ] [Лекции (видео)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)
        - начинается с таблицы символов и заканчивая BST приложениями
    - [ ] [Введение (видео)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
    - [ ] [MIT (видео)](https://www.youtube.com/watch?v=9Jry5-82I68)
    - C/C++:
        - [ ] [Бинарное дерево поиска - реализация на C/C++ (видео)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
        - [ ] [BST реализация - аллокация памяти в стеке и куче (видео)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
        - [ ] [Поиск минимального и максимального элемента в BST (видео)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Нахождение высоты BST (видео)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
        - [ ] [Обход BST - breadth-first и depth-first стратегии (видео)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
        - [ ] [Бинарное дерево: обход по уровням (видео)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Обход бинарного дерева: Pre-order, In-order, Post-order (видео)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Проверка - бинарное дерево BST или нет (видео)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Удаление узов в BST (видео)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
        - [ ] [In-order аналог в BST (видео)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] Реализация:
        - [ ] insert    // вставка значения в дерево
        - [ ] get_node_count // получение количества хранящихся значений
        - [ ] print_values // вывод значений, начиная с min к max
        - [ ] delete_tree
        - [ ] is_in_tree // возвращает если переданное значение есть в дереве
        - [ ] get_height // возвращает высоту дерева в количестве узлов (высота одного узла 1)
        - [ ] get_min   // возвращает минимальное значение хранящиеся в узлах дерева
        - [ ] get_max   // возвращает максимальное значение хранящиеся в узлах дерева
        - [ ] is_binary_search_tree
        - [ ] delete_value
        - [ ] get_successor // возвращает следующее максимальное значение в дереве после переданного, -1 если none

- ### Куча, Приоритетная очередь, Бинарная куча
    - визуализируется как дерево, но обычно хранится в линейных структурах данных (массив, связанные список)
    - [ ] [Куча](https://en.wikipedia.org/wiki/Heap_(data_structure))
    - [ ] [Введение (видео)](https://www.coursera.org/learn/data-structures/lecture/2OpTs/introduction)
    - [ ] [Наивная реализация (видео)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
    - [ ] [Бинарные деревья (видео)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
    - [ ] [Замечания к высоте дерева (видео)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
    - [ ] [Базовые операции (видео)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
    - [ ] [Полные двоичные деревья (видео)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
    - [ ] [Псевдокод (видео)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
    - [ ] [Пирамидальная сортировка - начальные шаги (видео)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
    - [ ] [Пирамидальная сортировка (видео)](https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort)
    - [ ] [Построение кучи (видео)](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)
    - [ ] [MIT: Кучи и пирамидальная сортировка (видео)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [CS 61B Лекция 24: Приоритетные очереди (видео)](https://www.youtube.com/watch?v=yIUFT6AKBGE&index=24&list=PL4BBB74C7D2A1049C)
    - [ ] [Построение кучи за линейное время (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
    - [ ] Реализация max-heap:
        - [ ] insert
        - [ ] sift_up - необходима для вставки
        - [ ] get_max - возвращает максимальный элемент, не удаляя его
        - [ ] get_size() - возвращает количество хранящихся элементов
        - [ ] is_empty() - возвращает true если куча пустая
        - [ ] extract_max - возвращает максимальный элемент, удаляя его
        - [ ] sift_down - необходима для extract_max
        - [ ] remove(i) - удаляет элемент по индексу x
        - [ ] heapify - создает кучу из элементов массива, необходима для heap_sort
        - [ ] heap_sort() - берет не отсортированный массив и делает его отсортированным, не используя дополнительной памяти, кроме занимаемой самим массивом используя max heap
            - важно: можно использовать min heap, но тогда понадобиться доболнительная память.