# PlainValidationResultItem - класс
Объект, свойства которого соответствуют элементу
[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm),
удобный для сериализации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PlainValidationResultItem
VB __Копировать
     Public NotInheritable Class PlainValidationResultItem
C++ __Копировать
     public ref class PlainValidationResultItem sealed
F# __Копировать
     [<SealedAttribute>]
    type PlainValidationResultItem = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlainValidationResultItem
##  __Конструкторы
[PlainValidationResultItem](M_Tessa_Platform_Validation_PlainValidationResultItem__ctor.htm)|
Инициализирует новый экземпляр класса PlainValidationResultItem  
---|---  
##  __Свойства
[Details](P_Tessa_Platform_Validation_PlainValidationResultItem_Details.htm)|
Дополнительная информация о сообщении, например, полный текст исключения, или
null, если дополнительная информация отсутствует.  
---|---  
[FieldName](P_Tessa_Platform_Validation_PlainValidationResultItem_FieldName.htm)|
Имя поля объекта, к которому относится сообщение валидации, или null, если
поле неизвестно.  
[Key](P_Tessa_Platform_Validation_PlainValidationResultItem_Key.htm)| Ключ
сообщения, возникшего при валидации.  
[Message](P_Tessa_Platform_Validation_PlainValidationResultItem_Message.htm)|
Текст сообщения, возникшего при валидации.  
[ObjectName](P_Tessa_Platform_Validation_PlainValidationResultItem_ObjectName.htm)|
Имя объекта, к которому относится сообщение валидации, или null, если имя
неизвестно.  
[ObjectType](P_Tessa_Platform_Validation_PlainValidationResultItem_ObjectType.htm)|
Тип объекта, к которому относится сообщение валидации, или null, если тип
неизвестен.  
[Type](P_Tessa_Platform_Validation_PlainValidationResultItem_Type.htm)|
Тип сообщения, возникшего при валидации.
0 \- информационное сообщение; 1 \- предупреждение; 2 \- ошибка.  
## __Методы
[Create](M_Tessa_Platform_Validation_PlainValidationResultItem_Create.htm)|
Создаёт объект, свойства которого заполняются в соответствии со значениями
[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm).  
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
[ToValidationResultItem](M_Tessa_Platform_Validation_PlainValidationResultItem_ToValidationResultItem.htm)|
Создаёт объект
[ValidationResultItem](T_Tessa_Platform_Validation_ValidationResultItem.htm)
по свойствам текущего объекта.  
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
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
