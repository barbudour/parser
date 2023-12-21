# IApplicationCatalogRegistry.Remove - метод
Удаляет компонент catalog из контейнера. Удаляемый компонент должен быть не
равен null
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void Remove(
    	[NotNullAttribute] IApplicationCatalog catalog
    )
VB __Копировать
     Sub Remove ( 
    	<NotNullAttribute> catalog As IApplicationCatalog
    )
C++ __Копировать
     void Remove(
    	[NotNullAttribute] IApplicationCatalog^ catalog
    )
F# __Копировать
     abstract Remove : 
            [<NotNullAttribute>] catalog : IApplicationCatalog -> unit 
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Удаляемый из контейнера компонент 
## __См. также
#### Ссылки
[IApplicationCatalogRegistry -
](T_Tessa_Applications_IApplicationCatalogRegistry.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
