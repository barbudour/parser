# ICardTaskTypePolicy.IsAllowed(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
задания с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	string taskTypeName
    )
VB __Копировать
     Function IsAllowed ( 
    	taskTypeName As String
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	String^ taskTypeName
    )
F# __Копировать
     abstract IsAllowed : 
            taskTypeName : string -> bool 
#### Параметры
taskTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для типа задания с заданным
именем; false в противном случае.
## __См. также
#### Ссылки
[ICardTaskTypePolicy - ](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
