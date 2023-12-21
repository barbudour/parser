# StageRowMigrationHelper - класс
Предоставляет методы позволяющие выполнить миграцию строк этапов из одной
карточки в другую.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class StageRowMigrationHelper
VB __Копировать
     Public NotInheritable Class StageRowMigrationHelper
C++ __Копировать
     public ref class StageRowMigrationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type StageRowMigrationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageRowMigrationHelper
##  __Методы
[GetSignatures](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageRowMigrationHelper_GetSignatures.htm)|
Возвращает информацию о подписи этапов или значение по умолчанию для типа,
если она не была найдена.  
---|---  
[MigrateAsync(Card, Card, KrProcessSerializerHiddenStageMode,
IKrStageSerializer, ICardMetadata, IGuidReplacer,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageRowMigrationHelper_MigrateAsync.htm)|
Выполняет миграцию этапов из карточки source в target.  
[MigrateAsync(Card, Card, KrProcessSerializerHiddenStageMode,
IKrStageSerializer, ICardMetadata, IGuidReplacer, ISignatureProvider,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageRowMigrationHelper_MigrateAsync_1.htm)|
Выполняет миграцию этапов из карточки source в target и выполняет их
подписание.  
[VerifyRow](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageRowMigrationHelper_VerifyRow.htm)|
Проверяет была ли строка этапа изменена.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
