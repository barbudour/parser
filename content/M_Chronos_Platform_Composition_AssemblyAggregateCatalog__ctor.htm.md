# AssemblyAggregateCatalog - конструктор
Создаёт экземпляр класса с указанием списка каталогов, из которых составляется
текущий каталог.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public AssemblyAggregateCatalog(
    	params IAssemblyCatalog[] catalogs
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray catalogs As IAssemblyCatalog()
    )
C++ __Копировать
     public:
    AssemblyAggregateCatalog(
    	... array<IAssemblyCatalog^>^ catalogs
    )
F# __Копировать
     new : 
            catalogs : IAssemblyCatalog[] -> AssemblyAggregateCatalog
#### Параметры
catalogs
[IAssemblyCatalog](T_Chronos_Platform_Composition_IAssemblyCatalog.htm)[]
     Список каталогов, из которых составляется текущий каталог. Не должен быть равен null. 
## __См. также
#### Ссылки
[AssemblyAggregateCatalog -
](T_Chronos_Platform_Composition_AssemblyAggregateCatalog.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
