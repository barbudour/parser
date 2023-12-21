# CardHeaderFile.IsEmpty - метод
Возвращает признак того, что объект не содержит значимых данных для метода
очистки [Tessa.Platform.Storage.IStorageCleanable.Clean].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsEmpty()
VB __Копировать
     Public Function IsEmpty As Boolean
C++ __Копировать
     public:
    bool IsEmpty()
F# __Копировать
     member IsEmpty : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект не содержит значимых для метода очистки данных; false в
противном случае.
## __Заметки
Метод следует вызывать только после выполнения
[Tessa.Platform.Storage.IStorageCleanable.Clean].
## __См. также
#### Ссылки
[CardHeaderFile - ](T_Tessa_Cards_ComponentModel_CardHeaderFile.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
