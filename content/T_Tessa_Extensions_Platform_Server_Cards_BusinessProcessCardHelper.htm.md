# BusinessProcessCardHelper - класс
Вспомогательные методы для работы с карточкой шаблона процесса
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class BusinessProcessCardHelper
VB __Копировать
     Public NotInheritable Class BusinessProcessCardHelper
C++ __Копировать
     public ref class BusinessProcessCardHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type BusinessProcessCardHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ BusinessProcessCardHelper
##  __Методы
[ClearLockInfo](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ClearLockInfo.htm)|  
---|---  
[CompressRow](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_CompressRow.htm)|
Метод для компресии данных в строке с версией процесса  
[DecompressRow](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_DecompressRow.htm)|
Метод для декомпресии данных в строке с версией процесса  
[FillNewVersionRow](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_FillNewVersionRow.htm)|
Метод для заполнения полей строки новой версии процесса  
[FillVirtualRow](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_FillVirtualRow.htm)|
Метод для переноса данных их строки физической секции версии процесса в строку
виртуальной секции  
[FillVirtualSection](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_FillVirtualSection.htm)|
Метод для заполнения виртуальной секции процесса из физической секции  
[FillVirtualSectionAsync](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_FillVirtualSectionAsync.htm)|
Метод для заполнения виртуальной секции версий процесса из базы  
[GetNextVersionAsync](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_GetNextVersionAsync.htm)|
Метод для получения следующего номера версии процесса  
[ModifyVersionRow](M_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ModifyVersionRow.htm)|
Метод для заполнения полей строки версии процесса, которые должны заполняться
при изменении процесса.  
## __Поля
[ActionNameFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ActionNameFieldName.htm)|  
---|---  
[ActionStorageFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ActionStorageFieldName.htm)|  
[BusinessProcessCardIDFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_BusinessProcessCardIDFieldName.htm)|  
[BusinessProcessRowIDFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_BusinessProcessRowIDFieldName.htm)|  
[MethodFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_MethodFieldName.htm)|  
[NewBlockStateFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_NewBlockStateFieldName.htm)|  
[ParametersFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ParametersFieldName.htm)|  
[ProcessInstanceIDFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ProcessInstanceIDFieldName.htm)|  
[ProcessVersionDataFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ProcessVersionDataFieldName.htm)|  
[ResultFieldName](F_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper_ResultFieldName.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
