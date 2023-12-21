# CardHeader.TryGetFiles - метод
Возвращает список прикреплённых к карточке файлов, содержимое которых
передаётся в потоке, или null, если список ещё не был задан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public GuidDictionaryStorage<CardHeaderFile> TryGetFiles()
VB __Копировать
     Public Function TryGetFiles As GuidDictionaryStorage(Of CardHeaderFile)
C++ __Копировать
     public:
    GuidDictionaryStorage<CardHeaderFile^>^ TryGetFiles()
F# __Копировать
     member TryGetFiles : unit -> GuidDictionaryStorage<CardHeaderFile> 
#### Возвращаемое значение
[GuidDictionaryStorage](T_Tessa_Platform_Storage_GuidDictionaryStorage_1.htm)<[CardHeaderFile](T_Tessa_Cards_ComponentModel_CardHeaderFile.htm)>  
Список прикреплённых к карточке файлов или null, если список ещё не был задан.
## __См. также
#### Ссылки
[CardHeader - ](T_Tessa_Cards_ComponentModel_CardHeader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
