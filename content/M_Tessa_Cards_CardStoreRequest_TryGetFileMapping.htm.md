# CardStoreRequest.TryGetFileMapping - метод
Возвращает маппинг для контента сохраняемых файлов или null, если маппинг ещё
не был задан. Значение актуально задавать при сохранении карточки с контентом
файлов, которые являются виртуальными, т.е. принадлежат другой карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardFileContentMapping> TryGetFileMapping()
VB __Копировать
     Public Function TryGetFileMapping As ListStorage(Of CardFileContentMapping)
C++ __Копировать
     public:
    ListStorage<CardFileContentMapping^>^ TryGetFileMapping()
F# __Копировать
     member TryGetFileMapping : unit -> ListStorage<CardFileContentMapping> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm)>  
Возвращает маппинг для контента сохраняемых файлов или null, если маппинг ещё
не был задан.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
