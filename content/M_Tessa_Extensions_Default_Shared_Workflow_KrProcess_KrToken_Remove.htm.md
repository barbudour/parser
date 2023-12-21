# KrToken.Remove(IDictionary<String, Object>) - метод
Удаляет информацию по токену безопасности
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
для заданной хеш-таблицы cardInfo. Возвращает признак того, что токен
присутствовал и был удалён.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool Remove(
    	IDictionary<string, Object> cardInfo
    )
VB __Копировать
     Public Shared Function Remove ( 
    	cardInfo As IDictionary(Of String, Object)
    ) As Boolean
C++ __Копировать
     public:
    static bool Remove(
    	IDictionary<String^, Object^>^ cardInfo
    )
F# __Копировать
     static member Remove : 
            cardInfo : IDictionary<string, Object> -> bool 
#### Параметры
cardInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация для карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если токен присутствовал в объекте cardInfo и был удалён; false, если
токен отсутствовал и не был удалён.
## __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Remove -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_Remove.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
