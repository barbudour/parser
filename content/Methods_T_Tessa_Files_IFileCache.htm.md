# IFileCache - методы
##  __Методы
[AllocateAsync](M_Tessa_Files_IFileCache_AllocateAsync.htm)| Создаёт объект,
инкапсулирующий контент файла в кэше.  
---|---  
[ClearAsync](M_Tessa_Files_IFileCache_ClearAsync.htm)| Очищает кэш, освобождая
все объекты, которые инкапсулируют контент файлов.  
[DisposeDelayedContentAsync](M_Tessa_Files_IFileCache_DisposeDelayedContentAsync.htm)|
Немедленно выполняет отложенное освобождение содержимого, если это требуется.  
[HasPendingDelayedContentDisposalAsync](M_Tessa_Files_IFileCache_HasPendingDelayedContentDisposalAsync.htm)|
Возвращает признак того, что кэш ожидает отложенное освобождение содержимого
хотя бы одного файла.  
[IsEmptyAsync](M_Tessa_Files_IFileCache_IsEmptyAsync.htm)|  Признак того, что
кэш пустой, т.е. не содержит объектов, инкапсулирующих контент файлов.  
[NotifyDelayedContentDisposalPendingAsync](M_Tessa_Files_IFileCache_NotifyDelayedContentDisposalPendingAsync.htm)|
Уведомляет кэш о необходимости выполнить отложенное освобождение содержимого
через некоторое время, если это требуется.  
[RegisterForDisposalAsync](M_Tessa_Files_IFileCache_RegisterForDisposalAsync.htm)|
Добавляет заданный объект контента к списку освобождаемых объектов при очистке
кэша (если кэш связан с карточкой - при закрытии или обновлении карточки).
Вызывайте метод для объектов, которые не созданы средствами этого же кэша.  
[ResetDelayedContentDisposalAsync](M_Tessa_Files_IFileCache_ResetDelayedContentDisposalAsync.htm)|
Очищает информацию о необходимости выполнить отложенное освобождение
содержимого. Файлы, которые не были удалены и требуют отложенного
освобождения, останутся во временной папке (или в другом местоположении) и не
будут удалены.  
## __См. также
#### Ссылки
[IFileCache - ](T_Tessa_Files_IFileCache.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
