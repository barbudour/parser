# KrToken.CardID - свойство
Идентификатор карточки. Если равен
[Empty](https://learn.microsoft.com/dotnet/api/system.guid.empty), то
считается, что токен подписан для любой карточки, что актуально, прежде всего,
для алгоритма создания карточки cardRepository.New().
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid CardID { get; set; }
VB __Копировать
     Public Property CardID As Guid
    	Get
    	Set
C++ __Копировать
     public:
    property Guid CardID {
    	Guid get ();
    	void set (Guid value);
    }
F# __Копировать
     member CardID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
