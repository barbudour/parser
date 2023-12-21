# StageOrderComparer - класс
Объект, выполняющий сортировку этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StageOrderComparer : Comparer<Stage>
VB __Копировать
     Public NotInheritable Class StageOrderComparer
    	Inherits Comparer(Of Stage)
C++ __Копировать
     public ref class StageOrderComparer sealed : public Comparer<Stage^>
F# __Копировать
     [<SealedAttribute>]
    type StageOrderComparer = 
        class
            inherit Comparer<Stage>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Comparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.comparer-1)<[Stage](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage.htm)> __ StageOrderComparer
##  __Заметки
Правило сортировки.
Сортировка сначала разделяет все этапы по группам. Сортировка для групп
происходит по паре
([StageGroupOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageGroupOrder.htm),
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageGroupID.htm)),
что позволяет получить уникальность каждого элемента и стабильность
сортировки.
В каждой группе проводится сортировка по следующим признакам:
[AtFirst](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtFirst.htm)
&
![CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
[AtFirst](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtFirst.htm)
&
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
[Unspecified](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Unspecified.htm)
&
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
[AtLast](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtLast.htm)
&
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
[AtLast](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtLast.htm)
&
![CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
[Unspecified](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Unspecified.htm)
&
![CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)
\- положение не меняют.
Внутри каждой такой подгруппы производится дополнительная сортировка по
[TemplateOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateOrder.htm).
Это поле хранит TemplateOrder из карточки шаблона этапов KrStageTemplates.
Данный
[TemplateOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateOrder.htm)
не имеет отношения к обычному Order в таблице этапов карточки.
Последним ключом сортировки является
[TemplateStageOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateStageOrder.htm)
этапов из шаблона. Это необходимо для переноса порядка сортировки из дочернего
маршрута шаблона в целый маршрут документа.
Важным свойством является стабильность [!:Enumerable.OrderBy<TSource,
TKey>(IEnumerable<TSource>, Func<TSource, TKey>)] сортировки. Источник:
https://docs.microsoft.com/ru-ru/dotnet/api/system.linq.enumerable.orderby
абзац "комментарии", предпоследнее предложение. "This method performs a stable
sort; that is, if the keys of two elements are equal, the order of the
elements is preserved." Это позволяет при сортировке сохранить порядок
Unspecified этапов таким, каким его указал пользователь.
## __Конструкторы
[StageOrderComparer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StageOrderComparer__ctor.htm)|
Инициализирует новый экземпляр класса StageOrderComparer  
---|---  
##  __Свойства
[Instance](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StageOrderComparer_Instance.htm)|  
---|---  
## __Методы
[Compare](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StageOrderComparer_Compare.htm)|
When overridden in a derived class, performs a comparison of two objects of
the same type and returns a value indicating whether one object is less than,
equal to, or greater than the other.  
(Переопределяет [Comparer<T>.Compare(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.comparer-1.compare#system-
collections-generic-comparer-1-compare\(-0-0\)))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)
#### Другие ресурсы
<https://mytessa.ru/docs/3.6/adm/admin/routes/#template-stages>
