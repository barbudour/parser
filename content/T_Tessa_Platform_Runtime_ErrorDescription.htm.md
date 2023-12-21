# ErrorDescription - класс
Описание ошибки, которое задаётся при работе с сервисом
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ErrorDescription : IErrorDescription
VB __Копировать
     Public NotInheritable Class ErrorDescription
    	Implements IErrorDescription
C++ __Копировать
     public ref class ErrorDescription sealed : IErrorDescription
F# __Копировать
     [<SealedAttribute>]
    type ErrorDescription = 
        class
            interface IErrorDescription
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ErrorDescription
Implements
    [IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm)
##  __Конструкторы
[ErrorDescription](M_Tessa_Platform_Runtime_ErrorDescription__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Category](P_Tessa_Platform_Runtime_ErrorDescription_Category.htm)| Категория
ошибки, обычно строка-алиас. Равно пустой строке, если категория не задана.  
---|---  
[Info](P_Tessa_Platform_Runtime_ErrorDescription_Info.htm)| Произвольная
информация, сериализуемая вместе с ошибкой.  
[Text](P_Tessa_Platform_Runtime_ErrorDescription_Text.htm)| Дополнительное
текстовое описание ошибки. Равно пустой строке, если описание не задано.  
[ValidationResult](P_Tessa_Platform_Runtime_ErrorDescription_ValidationResult.htm)|
Сообщения валидации.  
##  __Методы
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
