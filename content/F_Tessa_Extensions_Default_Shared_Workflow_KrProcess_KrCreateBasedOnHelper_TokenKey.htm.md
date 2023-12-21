# KrCreateBasedOnHelper.TokenKey - поле
Ключ, по которому в [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info
доступен токен безопасности
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
для карточки, на основании которой создаётся другая карточка, или null, если
токен отсутствует и права на чтение будут вычислены в процессе создания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string TokenKey = "KrCreateBasedOnToken"
VB __Копировать
     Public Const TokenKey As String = "KrCreateBasedOnToken"
C++ __Копировать
     public:
    literal String^ TokenKey = "KrCreateBasedOnToken"
F# __Копировать
     static val mutable TokenKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[KrCreateBasedOnHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
