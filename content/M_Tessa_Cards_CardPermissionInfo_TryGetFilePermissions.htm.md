# CardPermissionInfo.TryGetFilePermissions - метод
Возвращает права доступа на файлы, прикреплённые к карточке, или null, если
права ещё не были заданы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public GuidDictionaryStorage<CardPermissionFlags> TryGetFilePermissions()
VB __Копировать
     Public Function TryGetFilePermissions As GuidDictionaryStorage(Of CardPermissionFlags)
C++ __Копировать
     public:
    GuidDictionaryStorage<CardPermissionFlags>^ TryGetFilePermissions()
F# __Копировать
     member TryGetFilePermissions : unit -> GuidDictionaryStorage<CardPermissionFlags> 
#### Возвращаемое значение
[GuidDictionaryStorage](T_Tessa_Platform_Storage_GuidDictionaryStorage_1.htm)<[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)>  
Права доступа на файлы, прикреплённые к карточке, или null, если права ещё не
были заданы.
## __См. также
#### Ссылки
[CardPermissionInfo - ](T_Tessa_Cards_CardPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
