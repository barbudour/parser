# CardValidationHelper.RowPermissionsAreValid - метод
Проверяет, что права доступа на строку коллекционной или древовидной секции
являются валидными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool RowPermissionsAreValid(
    	CardPermissionFlags permissions
    )
VB __Копировать
     Public Shared Function RowPermissionsAreValid ( 
    	permissions As CardPermissionFlags
    ) As Boolean
C++ __Копировать
     public:
    static bool RowPermissionsAreValid(
    	CardPermissionFlags permissions
    )
F# __Копировать
     static member RowPermissionsAreValid : 
            permissions : CardPermissionFlags -> bool 
#### Параметры
permissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Права доступа на строку коллекционной или древовидной секции.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданные права доступа являются валидными для строки коллекционной
или древовидной секции; false в противном случае.
## __Заметки
Для строки коллекционной или древовидной секции валидны её собственные права
доступа и права на дочерние поля.
Недопустимо одновременное использование Allow и Prohibit флагов.
##  __См. также
#### Ссылки
[CardValidationHelper - ](T_Tessa_Cards_CardValidationHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
