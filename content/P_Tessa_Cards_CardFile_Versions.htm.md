# CardFile.Versions - свойство
Список версий файла. Загружается отложенно; список заполнен, если значение
[VersionsLoaded](P_Tessa_Cards_CardFile_VersionsLoaded.htm) равно true.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardFileVersion> Versions { get; set; }
VB __Копировать
     Public Property Versions As ListStorage(Of CardFileVersion)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardFileVersion^>^ Versions {
    	ListStorage<CardFileVersion^>^ get ();
    	void set (ListStorage<CardFileVersion^>^ value);
    }
F# __Копировать
     member Versions : ListStorage<CardFileVersion> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)>
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
