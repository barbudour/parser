# CardFileContentMapping.RepairStorage - метод
Исправляет хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RepairStorage()
VB __Копировать
     Public Function RepairStorage As Boolean
C++ __Копировать
     public:
    bool RepairStorage()
F# __Копировать
     member RepairStorage : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если при исправлении в объект были внесены изменения; false в противном
случае.
## __См. также
#### Ссылки
[CardFileContentMapping - ](T_Tessa_Cards_CardFileContentMapping.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
