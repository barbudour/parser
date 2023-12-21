# CardValidationHelper.FilePermissionsAreValid - метод
Проверяет, что права доступа на файл, прикреплённый к карточке, являются
валидными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool FilePermissionsAreValid(
    	CardPermissionFlags permissions
    )
VB __Копировать
     Public Shared Function FilePermissionsAreValid ( 
    	permissions As CardPermissionFlags
    ) As Boolean
C++ __Копировать
     public:
    static bool FilePermissionsAreValid(
    	CardPermissionFlags permissions
    )
F# __Копировать
     static member FilePermissionsAreValid : 
            permissions : CardPermissionFlags -> bool 
#### Параметры
permissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Права доступа на файл, прикреплённый к карточке.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданные права доступа являются валидными для файла, прикреплённого
к карточке; false в противном случае.
## __Заметки
Для файла, прикреплённого к карточке, валидны только его собственные права
доступа.
Недопустимо одновременное использование Allow и Prohibit флагов.
##  __См. также
#### Ссылки
[CardValidationHelper - ](T_Tessa_Cards_CardValidationHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
