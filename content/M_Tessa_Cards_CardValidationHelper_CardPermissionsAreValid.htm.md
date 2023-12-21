# CardValidationHelper.CardPermissionsAreValid - метод
Проверяет, что права доступа на карточку являются валидными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CardPermissionsAreValid(
    	CardPermissionFlags permissions
    )
VB __Копировать
     Public Shared Function CardPermissionsAreValid ( 
    	permissions As CardPermissionFlags
    ) As Boolean
C++ __Копировать
     public:
    static bool CardPermissionsAreValid(
    	CardPermissionFlags permissions
    )
F# __Копировать
     static member CardPermissionsAreValid : 
            permissions : CardPermissionFlags -> bool 
#### Параметры
permissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Права доступа на карточку.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданные права доступа являются валидными для карточки; false в
противном случае.
## __Заметки
Для карточки валидны любые права доступа, т.к. неприменимые к карточке права
будут использоваться в одном из её дочерних элементов (таких, как секция,
строка, поле или прикреплённый файл).
Недопустимо одновременное использование Allow и Prohibit флагов.
##  __См. также
#### Ссылки
[CardValidationHelper - ](T_Tessa_Cards_CardValidationHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
