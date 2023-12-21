# IComponent<TOperation>.Accept - метод
Вызывает выполнение операции operation над текущим узлом
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void Accept(
    	[NotNullAttribute] TOperation operation,
    	[NotNullAttribute] IOperationContext operationContext
    )
VB __Копировать
     Sub Accept ( 
    	<NotNullAttribute> operation As TOperation,
    	<NotNullAttribute> operationContext As IOperationContext
    )
C++ __Копировать
     void Accept(
    	[NotNullAttribute] TOperation operation, 
    	[NotNullAttribute] IOperationContext^ operationContext
    )
F# __Копировать
     abstract Accept : 
            [<NotNullAttribute>] operation : 'TOperation * 
            [<NotNullAttribute>] operationContext : IOperationContext -> unit 
#### Параметры
operation [TOperation](T_Tessa_Applications_Containers_IComponent_1.htm)
     Операция над компонентами 
operationContext
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm)
     Контекст операции 
## __См. также
#### Ссылки
[IComponent<TOperation> \- ](T_Tessa_Applications_Containers_IComponent_1.htm)
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
