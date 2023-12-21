# KrToken.Contains - метод
Возвращает признак того, что в заданной хеш-таблице cardInfo содержится
информация по токену безопасности.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool Contains(
    	IDictionary<string, Object> cardInfo
    )
VB __Копировать
     Public Shared Function Contains ( 
    	cardInfo As IDictionary(Of String, Object)
    ) As Boolean
C++ __Копировать
     public:
    static bool Contains(
    	IDictionary<String^, Object^>^ cardInfo
    )
F# __Копировать
     static member Contains : 
            cardInfo : IDictionary<string, Object> -> bool 
#### Параметры
cardInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация для карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в заданной хеш-таблице cardInfo содержится информация по токену
безопасности; false в противном случае.
## __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
