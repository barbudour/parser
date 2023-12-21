# KrPermissionsHelper.GetPermissionsSplittedByNewLineStartsWithNewLine - метод
Возвращает локализованные разрешения разделенные переводом на новую строку.
Начинает новой строкой.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetPermissionsSplittedByNewLineStartsWithNewLine(
    	params KrPermissionFlagDescriptor[] permissions
    )
VB __Копировать
     Public Shared Function GetPermissionsSplittedByNewLineStartsWithNewLine ( 
    	ParamArray permissions As KrPermissionFlagDescriptor()
    ) As String
C++ __Копировать
     public:
    static String^ GetPermissionsSplittedByNewLineStartsWithNewLine(
    	... array<KrPermissionFlagDescriptor^>^ permissions
    )
F# __Копировать
     static member GetPermissionsSplittedByNewLineStartsWithNewLine : 
            permissions : KrPermissionFlagDescriptor[] -> string 
#### Параметры
permissions
[KrPermissionFlagDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionFlagDescriptor.htm)[]
    Разрешения, которые нужно локализовать и перечислить.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Локализованные разрешения разделенные переводом на новую строку. Начинает
новой строкой.
##  __См. также
#### Ссылки
[KrPermissionsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
