# AdvancedFilterViewDialogManager - класс
Объект, предоставляющий методы для открытия модального диалога с параметрами
фильтрации представления.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Views](N_Tessa_Extensions_Default_Client_Views.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class AdvancedFilterViewDialogManager : IAdvancedFilterViewDialogManager
VB __Копировать
     Public Class AdvancedFilterViewDialogManager
    	Implements IAdvancedFilterViewDialogManager
C++ __Копировать
     public ref class AdvancedFilterViewDialogManager : IAdvancedFilterViewDialogManager
F# __Копировать
     type AdvancedFilterViewDialogManager = 
        class
            interface IAdvancedFilterViewDialogManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AdvancedFilterViewDialogManager
Implements
    [IAdvancedFilterViewDialogManager](T_Tessa_Extensions_Default_Client_Views_IAdvancedFilterViewDialogManager.htm)
##  __Конструкторы
[AdvancedFilterViewDialogManager](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Методы
[AddParameterIfValueNotEmpty](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_AddParameterIfValueNotEmpty.htm)|
Добавляет параметр в запрос к представлению, если поле
[ValueFieldName](P_Tessa_Extensions_Default_Client_Views_ParameterMapping_ValueFieldName.htm)
в секции
[ValueSectionName](P_Tessa_Extensions_Default_Client_Views_ParameterMapping_ValueSectionName.htm)
содержит данные.  
---|---  
[CreateDialogCardModelAsync](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_CreateDialogCardModelAsync.htm)|
Создаёт модель карточки диалога, содержащего параметры представления.  
[CreateParameters](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_CreateParameters.htm)|
Создаёт параметры запроса к представлению.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillField](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_FillField.htm)|
Заполняет поле
[ValueFieldName](P_Tessa_Extensions_Default_Client_Views_ParameterMapping_ValueFieldName.htm)
в секции
[ValueSectionName](P_Tessa_Extensions_Default_Client_Views_ParameterMapping_ValueSectionName.htm),
содержащее параметр фильтрации представления
[Alias](P_Tessa_Extensions_Default_Client_Views_ParameterMapping_Alias.htm).  
[FillFields](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_FillFields.htm)|
Заполняет поля карточки, данными параметров запроса к представлению.  
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
[OpenAsync](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_OpenAsync.htm)|
Открывает диалог с параметрами фильтрации представления.  
[ShowDialogAsync](M_Tessa_Extensions_Default_Client_Views_AdvancedFilterViewDialogManager_ShowDialogAsync.htm)|
Отображает диалог, содержащий параметры фильтрации представления.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Default.Client.Views - пространство
имён](N_Tessa_Extensions_Default_Client_Views.htm)
