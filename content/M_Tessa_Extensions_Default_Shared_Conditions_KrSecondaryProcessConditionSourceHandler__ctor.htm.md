# KrSecondaryProcessConditionSourceHandler - конструктор
Создаёт экземпляр класса с указанием его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Conditions](N_Tessa_Extensions_Default_Shared_Conditions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrSecondaryProcessConditionSourceHandler(
    	[OptionalDependencyAttribute] IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    KrSecondaryProcessConditionSourceHandler(
    	[OptionalDependencyAttribute] IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?dbScope : IDbScope 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
    *)
    -> KrSecondaryProcessConditionSourceHandler
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
    Объект для взаимодействия с базой данных. Может быть не задан, если обработчик используется на клиентской стороне.
##  __См. также
#### Ссылки
[KrSecondaryProcessConditionSourceHandler -
](T_Tessa_Extensions_Default_Shared_Conditions_KrSecondaryProcessConditionSourceHandler.htm)
[Tessa.Extensions.Default.Shared.Conditions - пространство
имён](N_Tessa_Extensions_Default_Shared_Conditions.htm)
