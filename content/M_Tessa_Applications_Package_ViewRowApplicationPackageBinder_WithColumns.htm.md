# ViewRowApplicationPackageBinder.WithColumns - метод
Устанавливает источник имен столбцов для вычисления расположение данных в
строке результата
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public ViewRowApplicationPackageBinder WithColumns(
    	[NotNullAttribute] IEnumerable<Object> columnNames
    )
VB __Копировать
    <NotNullAttribute>
    Public Function WithColumns ( 
    	<NotNullAttribute> columnNames As IEnumerable(Of Object)
    ) As ViewRowApplicationPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    ViewRowApplicationPackageBinder^ WithColumns(
    	[NotNullAttribute] IEnumerable<Object^>^ columnNames
    )
F# __Копировать
     [<NotNullAttribute>]
    member WithColumns : 
            [<NotNullAttribute>] columnNames : IEnumerable<Object> -> ViewRowApplicationPackageBinder 
#### Параметры
columnNames
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Список имен столбцов 
#### Возвращаемое значение
[ViewRowApplicationPackageBinder](T_Tessa_Applications_Package_ViewRowApplicationPackageBinder.htm)  
Возвращает себя в качестве результата исполнения
## __См. также
#### Ссылки
[ViewRowApplicationPackageBinder -
](T_Tessa_Applications_Package_ViewRowApplicationPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
