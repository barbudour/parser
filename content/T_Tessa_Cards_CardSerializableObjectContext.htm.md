# CardSerializableObjectContext - класс
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardSerializableObjectContext : ICardSerializableObjectContext
VB __Копировать
     Public NotInheritable Class CardSerializableObjectContext
    	Implements ICardSerializableObjectContext
C++ __Копировать
     public ref class CardSerializableObjectContext sealed : ICardSerializableObjectContext
F# __Копировать
     [<SealedAttribute>]
    type CardSerializableObjectContext = 
        class
            interface ICardSerializableObjectContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardSerializableObjectContext
Implements
    [ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm)
##  __Конструкторы
[CardSerializableObjectContext](M_Tessa_Cards_CardSerializableObjectContext__ctor.htm)|
Создаёт новый контекст.  
---|---  
## __Свойства
[Current](P_Tessa_Cards_CardSerializableObjectContext_Current.htm)|  Текущий
контекст
[ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm).  
---|---  
[GlobalReferences](P_Tessa_Cards_CardSerializableObjectContext_GlobalReferences.htm)|
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.  
[HasCurrent](P_Tessa_Cards_CardSerializableObjectContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm),
а свойство [Current](P_Tessa_Cards_CardSerializableObjectContext_Current.htm)
ссылается на действительный контекст.  
[Unknown](P_Tessa_Cards_CardSerializableObjectContext_Unknown.htm)|
Неизвестный контекст
[IFileResolverContext](T_Tessa_Files_IFileResolverContext.htm).  
## __Методы
[Create](M_Tessa_Cards_CardSerializableObjectContext_Create.htm)|  Создаёт
область операции, в которой заданный контекст будет являться текущим.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
