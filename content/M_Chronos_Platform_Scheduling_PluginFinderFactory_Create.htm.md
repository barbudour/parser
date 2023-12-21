# PluginFinderFactory.Create - метод
Создаёт объект, позволяющий осуществлять поиск плагинов в указанном каталоге.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IPluginFinder Create(
    	IAssemblyCatalog catalog
    )
VB __Копировать
     Public Shared Function Create ( 
    	catalog As IAssemblyCatalog
    ) As IPluginFinder
C++ __Копировать
     public:
    static IPluginFinder^ Create(
    	IAssemblyCatalog^ catalog
    )
F# __Копировать
     static member Create : 
            catalog : IAssemblyCatalog -> IPluginFinder 
#### Параметры
catalog
[IAssemblyCatalog](T_Chronos_Platform_Composition_IAssemblyCatalog.htm)
    Каталог, в котором будут найдены плагины.
#### Возвращаемое значение
[IPluginFinder](T_Chronos_Platform_Scheduling_IPluginFinder.htm)  
Объект, позволяющий осуществлять поиск плагинов.
##  __См. также
#### Ссылки
[PluginFinderFactory -
](T_Chronos_Platform_Scheduling_PluginFinderFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
