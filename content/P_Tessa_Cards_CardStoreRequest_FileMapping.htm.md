# CardStoreRequest.FileMapping - свойство
Маппинг для контента сохраняемых файлов. Значение актуально задавать при
сохранении карточки с контентом файлов, которые являются виртуальными, т.е.
принадлежат другой карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardFileContentMapping> FileMapping { get; set; }
VB __Копировать
     Public Property FileMapping As ListStorage(Of CardFileContentMapping)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardFileContentMapping^>^ FileMapping {
    	ListStorage<CardFileContentMapping^>^ get ();
    	void set (ListStorage<CardFileContentMapping^>^ value);
    }
F# __Копировать
     member FileMapping : ListStorage<CardFileContentMapping> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm)>
##  __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
