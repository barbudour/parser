# PluginFactory.CreatePlugin - метод
Создаёт экземпляр плагина, который соответствует указанному типу typeFullName,
загруженному из указанной сборки assembly.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IPlugin CreatePlugin(
    	Assembly assembly,
    	string typeFullName
    )
VB __Копировать
     Public Shared Function CreatePlugin ( 
    	assembly As Assembly,
    	typeFullName As String
    ) As IPlugin
C++ __Копировать
     public:
    static IPlugin^ CreatePlugin(
    	Assembly^ assembly, 
    	String^ typeFullName
    )
F# __Копировать
     static member CreatePlugin : 
            assembly : Assembly * 
            typeFullName : string -> IPlugin 
#### Параметры
assembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
     Сборка, в которой расположен создаваемый плагин. Не должна быть равна null. 
typeFullName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полное имя типа плагина, который располагается в указанной сборке.
#### Возвращаемое значение
[IPlugin](T_Chronos_Contracts_IPlugin.htm)  
Созданный экземпляр плагина.
##  __См. также
#### Ссылки
[PluginFactory - ](T_Chronos_Platform_Scheduling_PluginFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
