# ExtensionContainer.RegisterStrategy - метод
Регистрирует стратегию в контейнере. Существующая регистрация замещается.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IExtensionContainer RegisterStrategy(
    	ExtensionStrategyStage stage,
    	IExtensionStrategy strategy
    )
VB __Копировать
     Public Function RegisterStrategy ( 
    	stage As ExtensionStrategyStage,
    	strategy As IExtensionStrategy
    ) As IExtensionContainer
C++ __Копировать
     public:
    virtual IExtensionContainer^ RegisterStrategy(
    	ExtensionStrategyStage stage, 
    	IExtensionStrategy^ strategy
    ) sealed
F# __Копировать
     abstract RegisterStrategy : 
            stage : ExtensionStrategyStage * 
            strategy : IExtensionStrategy -> IExtensionContainer 
    override RegisterStrategy : 
            stage : ExtensionStrategyStage * 
            strategy : IExtensionStrategy -> IExtensionContainer 
#### Параметры
stage [ExtensionStrategyStage](T_Tessa_Extensions_ExtensionStrategyStage.htm)
    Этап выполнения стратегии.
strategy [IExtensionStrategy](T_Tessa_Extensions_IExtensionStrategy.htm)
    Стратегия, выполняемая на заданном этапе.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Контейнер для цепочки вызовов.
#### Реализации
[IExtensionContainer.RegisterStrategy(ExtensionStrategyStage,
IExtensionStrategy)](M_Tessa_Extensions_IExtensionContainer_RegisterStrategy.htm)  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр strategy равен null.  
---|---  
## __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
