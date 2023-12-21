# CardValidationHelper.TablePermissionsAreValid - метод
Проверяет, что права доступа на коллекционную или древовидную секцию являются
валидными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TablePermissionsAreValid(
    	CardPermissionFlags permissions
    )
VB __Копировать
     Public Shared Function TablePermissionsAreValid ( 
    	permissions As CardPermissionFlags
    ) As Boolean
C++ __Копировать
     public:
    static bool TablePermissionsAreValid(
    	CardPermissionFlags permissions
    )
F# __Копировать
     static member TablePermissionsAreValid : 
            permissions : CardPermissionFlags -> bool 
#### Параметры
permissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Права доступа на коллекционную или древовидную секцию.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданные права доступа являются валидными для коллекционной или
древовидной секции; false в противном случае.
## __Заметки
Для коллекционной или древовидной секции валидны её собственные права доступа
и права на дочерние строки и поля.
Недопустимо одновременное использование Allow и Prohibit флагов.
##  __См. также
#### Ссылки
[CardValidationHelper - ](T_Tessa_Cards_CardValidationHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
