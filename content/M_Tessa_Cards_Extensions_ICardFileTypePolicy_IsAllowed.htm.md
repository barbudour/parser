# ICardFileTypePolicy.IsAllowed(String) - метод
Возвращает признак того, что выполнение методов расширения допустимо для типа
файла с заданным именем.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	string fileTypeName
    )
VB __Копировать
     Function IsAllowed ( 
    	fileTypeName As String
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	String^ fileTypeName
    )
F# __Копировать
     abstract IsAllowed : 
            fileTypeName : string -> bool 
#### Параметры
fileTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа файла.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для типа файла с заданным
именем; false в противном случае.
## __См. также
#### Ссылки
[ICardFileTypePolicy - ](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_ICardFileTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
