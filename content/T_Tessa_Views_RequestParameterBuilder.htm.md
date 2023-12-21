# RequestParameterBuilder - класс
Построитель параметра запроса к представлению
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class RequestParameterBuilder
VB __Копировать
     Public Class RequestParameterBuilder
C++ __Копировать
     public ref class RequestParameterBuilder
F# __Копировать
     type RequestParameterBuilder = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RequestParameterBuilder
##  __Конструкторы
[RequestParameterBuilder(Boolean)](M_Tessa_Views_RequestParameterBuilder__ctor.htm)|
Initializes a new instance of the RequestParameterBuilder class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
[RequestParameterBuilder(RequestParameter)](M_Tessa_Views_RequestParameterBuilder__ctor_1.htm)|
Initializes a new instance of the RequestParameterBuilder class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
## __Методы
[AddCriteria(CriteriaOperator)](M_Tessa_Views_RequestParameterBuilder_AddCriteria.htm)|
Добавляет указанное условие к параметру.  
---|---  
[AddCriteria(RequestCriteria)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_8.htm)|
Добавляет указанное условие к параметру.  
[AddCriteria(ZeroValuesCriteriaOperator)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_7.htm)|
Добавляет указанное условие к параметру.  
[AddCriteria(CriteriaOperator, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_1.htm)|  Добавляет
указанное условие со значениями к параметру. Если указанный условный оператор
criteriaOperator не предполагает наличие значений, то к параметру будет
добавлено только условный оператор, с пустым списком значений  
[AddCriteria(OneValueCriteriaOperator, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_5.htm)|  Добавляет
указанное условие со значениями к параметру.  
[AddCriteria(CriteriaOperator, String, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_3.htm)|  Добавляет
указанное условие со значениями к параметру. Если указанный условный оператор
criteriaOperator не предполагает наличие значений, то к параметру будет
добавлено только условный оператор, с пустым списком значений  
[AddCriteria(OneValueCriteriaOperator, String, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_6.htm)|  Добавляет
указанное условие со значениями к параметру.  
[AddCriteria(CriteriaOperator, String, Object, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_2.htm)|  Добавляет
указанное условие со значениями к параметру. Если указанный условный оператор
criteriaOperator не предполагает наличие значений, то к параметру будет
добавлено только условный оператор, с пустым списком значений. Если указанный
оператор поддерживает меньшее количество значений, то переведенные значения
будут усечены до меньшего количества.  
[AddCriteria(CriteriaOperator, String, String, Object, String, String,
Object)](M_Tessa_Views_RequestParameterBuilder_AddCriteria_4.htm)|  Добавляет
указанное условие со значениями к параметру. Если указанный условный оператор
criteriaOperator не предполагает наличие значений, то к параметру будет
добавлено только условный оператор, с пустым списком значений. Если указанный
оператор поддерживает меньшее количество значений, то переведенные значения
будут усечены до меньшего количества.  
[AsRequestParameter](M_Tessa_Views_RequestParameterBuilder_AsRequestParameter.htm)|
Преобразует построитель в параметр запроса  
[ClearValues](M_Tessa_Views_RequestParameterBuilder_ClearValues.htm)|
Осуществляет очистку списка значений  
[CreateDefaultValues](M_Tessa_Views_RequestParameterBuilder_CreateDefaultValues.htm)|
Создает пустой список параметров  
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
[WithMetadata](M_Tessa_Views_RequestParameterBuilder_WithMetadata.htm)|
Устанавливает метаданные параметра  
## __Методы расширения
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
