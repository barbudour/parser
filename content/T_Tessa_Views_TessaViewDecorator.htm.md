# TessaViewDecorator - класс
Декорирует классы [представлений](T_Tessa_Views_ITessaView.htm) добавляет
функционал автоматического внедрения в список параметров
[запроса](T_Tessa_Views_ITessaViewRequest.htm) параметра [Идентификатор
текущего
пользователя](F_Tessa_Views_ViewSpecialParametersConst_CurrentUserId.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaViewDecorator : ITessaView, 
    	ITessaViewAccess, IViewTextGenerator
VB __Копировать
     Public Class TessaViewDecorator
    	Implements ITessaView, ITessaViewAccess, IViewTextGenerator
C++ __Копировать
     public ref class TessaViewDecorator : ITessaView, 
    	ITessaViewAccess, IViewTextGenerator
F# __Копировать
     type TessaViewDecorator = 
        class
            interface ITessaView
            interface ITessaViewAccess
            interface IViewTextGenerator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaViewDecorator
Implements
    [ITessaView](T_Tessa_Views_ITessaView.htm), [ITessaViewAccess](T_Tessa_Views_ITessaViewAccess.htm), [IViewTextGenerator](T_Tessa_Views_IViewTextGenerator.htm)
##  __Конструкторы
[TessaViewDecorator](M_Tessa_Views_TessaViewDecorator__ctor.htm)|  Initializes
a new instance of the TessaViewDecorator class.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDataAsync](M_Tessa_Views_TessaViewDecorator_GetDataAsync.htm)|  Выполняет
получение данных из представления на основании полученного
[запроса](T_Tessa_Views_ITessaViewRequest.htm)  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetadataAsync](M_Tessa_Views_TessaViewDecorator_GetMetadataAsync.htm)|
Возвращает метаданные представления. При первом обращении обычно выполняется
построение метаинформации.  
[GetRoles](M_Tessa_Views_TessaViewDecorator_GetRoles.htm)|  Возвращает список
ролей которые необходимы для доступа к представлению реализующему данный
интерфейс  
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
[TryGenerateAsync](M_Tessa_Views_TessaViewDecorator_TryGenerateAsync.htm)|
Осуществляет попытку генерации текста SQL запроса к представлению по запросу
request. Если представление не существует или не поддерживает генерацию текста
запроса(программные представления), то будет возвращена пустая строка.
Экземпляр представления по которому необходимо сгенерировать текст запроса
выбирается из request.Alias  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
