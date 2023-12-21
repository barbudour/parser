# KrToken.ExpiryDate - свойство
Дата и время истечения токена.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public DateTime ExpiryDate { get; set; }
VB __Копировать
     Public Property ExpiryDate As DateTime
    	Get
    	Set
C++ __Копировать
     public:
    property DateTime ExpiryDate {
    	DateTime get ();
    	void set (DateTime value);
    }
F# __Копировать
     member ExpiryDate : DateTime with get, set
#### Значение свойства
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
##  __Заметки
Рекомендуется устанавливать дату истечения на два дня большую, чем текущая
дата.
## __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
