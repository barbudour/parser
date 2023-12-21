# CardAnyTaskTypePolicy.IsAllowed(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
задания с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	string taskTypeName
    )
VB __Копировать
     Public Function IsAllowed ( 
    	taskTypeName As String
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	String^ taskTypeName
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            taskTypeName : string -> bool 
    override IsAllowed : 
            taskTypeName : string -> bool 
#### Параметры
taskTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для типа задания с заданным
именем; false в противном случае.
#### Реализации
[ICardTaskTypePolicy.IsAllowed(String)](M_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowed.htm)  
##  __См. также
#### Ссылки
[CardAnyTaskTypePolicy - ](T_Tessa_Cards_Extensions_CardAnyTaskTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_CardAnyTaskTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
