# CardFile.TryGetVersions - метод
Возвращает список версий файла или null, если список версий файла ещё не был
задан или не был загружен.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardFileVersion> TryGetVersions()
VB __Копировать
     Public Function TryGetVersions As ListStorage(Of CardFileVersion)
C++ __Копировать
     public:
    ListStorage<CardFileVersion^>^ TryGetVersions()
F# __Копировать
     member TryGetVersions : unit -> ListStorage<CardFileVersion> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)>  
Список версий файла или null, если список версий файла ещё не был задан или не
был загружен.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
