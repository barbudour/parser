# KrProcessSharedHelper.DesignTimeCard - метод
Возвращает значение, показывающее, может ли указанный тип карточки содержать
шаблоны этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool DesignTimeCard(
    	Guid typeID
    )
VB __Копировать
     Public Shared Function DesignTimeCard ( 
    	typeID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool DesignTimeCard(
    	Guid typeID
    )
F# __Копировать
     static member DesignTimeCard : 
            typeID : Guid -> bool 
#### Параметры
typeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если указанный тип карточки может содержать шаблоны этапов,
иначе - false.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
