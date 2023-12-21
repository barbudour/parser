# CardPermissionInfo.FilePermissions - свойство
Права доступа на файлы, прикреплённые к карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public GuidDictionaryStorage<CardPermissionFlags> FilePermissions { get; set; }
VB __Копировать
     Public Property FilePermissions As GuidDictionaryStorage(Of CardPermissionFlags)
    	Get
    	Set
C++ __Копировать
     public:
    property GuidDictionaryStorage<CardPermissionFlags>^ FilePermissions {
    	GuidDictionaryStorage<CardPermissionFlags>^ get ();
    	void set (GuidDictionaryStorage<CardPermissionFlags>^ value);
    }
F# __Копировать
     member FilePermissions : GuidDictionaryStorage<CardPermissionFlags> with get, set
#### Значение свойства
[GuidDictionaryStorage](T_Tessa_Platform_Storage_GuidDictionaryStorage_1.htm)<[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)>
##  __Заметки
Ключами в хеш-таблице должно являться свойство
[RowID](P_Tessa_Cards_CardFile_RowID.htm) соответствующих файлов.
## __См. также
#### Ссылки
[CardPermissionInfo - ](T_Tessa_Cards_CardPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
