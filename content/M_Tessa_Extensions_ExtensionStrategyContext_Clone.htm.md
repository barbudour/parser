# ExtensionStrategyContext.Clone - метод
Выполняет поверхностную копию объекта всех полей объекта, кроме контейнера
политик [Tessa.Extensions.IExtensionStrategyContext.Policies], для которого
копирование зависит от shallowClone.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IExtensionStrategyContext Clone(
    	bool shallowClone = false
    )
VB __Копировать
     Public Function Clone ( 
    	Optional shallowClone As Boolean = false
    ) As IExtensionStrategyContext
C++ __Копировать
     public:
    virtual IExtensionStrategyContext^ Clone(
    	bool shallowClone = false
    ) sealed
F# __Копировать
     abstract Clone : 
            ?shallowClone : bool 
    (* Defaults:
            let _shallowClone = defaultArg shallowClone false
    *)
    -> IExtensionStrategyContext 
    override Clone : 
            ?shallowClone : bool 
    (* Defaults:
            let _shallowClone = defaultArg shallowClone false
    *)
    -> IExtensionStrategyContext 
#### Параметры
shallowClone [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Выполнить поверхностную копию контейнера политик [Tessa.Extensions.IExtensionStrategyContext.Policies]
#### Возвращаемое значение
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)  
Копия объекта.
#### Реализации
[IExtensionStrategyContext.Clone(Boolean)](M_Tessa_Extensions_IExtensionStrategyContext_Clone.htm)  
##  __См. также
#### Ссылки
[ExtensionStrategyContext - ](T_Tessa_Extensions_ExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
