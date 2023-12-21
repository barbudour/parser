# CardFileSourceOverrideProvider - конструктор
Создаёт экземпляр с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileSourceOverrideProvider(
    	[OptionalDependencyAttribute] IConfigurationManager configurationManager = null
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> Optional configurationManager As IConfigurationManager = Nothing
    )
C++ __Копировать
     public:
    CardFileSourceOverrideProvider(
    	[OptionalDependencyAttribute] IConfigurationManager^ configurationManager = nullptr
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] ?configurationManager : IConfigurationManager 
    (* Defaults:
            let _configurationManager = defaultArg configurationManager null
    *)
    -> CardFileSourceOverrideProvider
#### Параметры
configurationManager
[IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm) (Optional)
     Объект, управляющий конфигурацией приложения, или null, если конфигурация недоступна. 
## __См. также
#### Ссылки
[CardFileSourceOverrideProvider -
](T_Tessa_Cards_CardFileSourceOverrideProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
