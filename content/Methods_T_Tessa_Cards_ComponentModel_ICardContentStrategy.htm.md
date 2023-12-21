# ICardContentStrategy - методы
##  __Методы
[CleanCardAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_CleanCardAsync.htm)|
Очищает место, отведённое для контента файлов, принадлежащих карточке. Метод
вызывается перед удалением карточки.  
---|---  
[CleanFileAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_CleanFileAsync.htm)|
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.  
[CopyAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_CopyAsync.htm)|
Выполняет копирование контента из исходного местоположения в целевое. Если
исходное и целевое местоположения совпадут, то метод завершится с ошибкой и
вернёт false.  
[DeleteAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_DeleteAsync.htm)|
Удаляет контент версии файла.  
[GetAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_GetAsync.htm)|
Загружает контент версии файла.  
[GetSizeAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_GetSizeAsync.htm)|
Возвращает длину контента версии файла в байтах.  
[MoveAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_MoveAsync.htm)|
Перемещает контент файла (но не записи по файлу) из исходного местоположения
sourceContext в целевое местоположение targetContext. При этом файл может
перемещаться между карточками и между разными файловыми хранилищами (если
текущая стратегия поддерживает разные хранилища). Если исходное и целевое
местоположения совпадают, то метод не выполняет действий и возвращает true.  
[MoveFileAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_MoveFileAsync.htm)|
Перемещает контент файла sourceFileID (но не записи по файлу) из карточки с
идентификатором sourceCardID в файл targetFileID в карточку с идентификатором
targetCardID. Содержимое не может быть перемещено между разными хранилищами
посредством этого метода, для этого долежн быть создан файл, в который
копируется содержимое исходного файла.  
[MoveFilesAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_MoveFilesAsync.htm)|
Перемещает контент файлов из карточки с идентификатором sourceCardID в
карточку с идентификатором targetCardID. При этом записи в секции по файлам не
перемещаются между карточками, для этого используйте методы
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFiles] или
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFilesAndSetTask].
Содержимое не может быть перемещено между разными хранилищами посредством
этого метода, для этого долежн быть создан файл, в который копируется
содержимое исходного файла.  
[StoreAsync](M_Tessa_Cards_ComponentModel_ICardContentStrategy_StoreAsync.htm)|
Сохраняет контент версии файла.  
##  __См. также
#### Ссылки
[ICardContentStrategy -
](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
