# NumberComposerDependencies - класс
Объект, содержащий зависимости стандартных классов, реализующих
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm). Классы-
наследники могут добавить дополнительные свойства, специфичные, например, для
типов карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NumberComposerDependencies : INumberComposerDependencies
VB __Копировать
     Public Class NumberComposerDependencies
    	Implements INumberComposerDependencies
C++ __Копировать
     public ref class NumberComposerDependencies : INumberComposerDependencies
F# __Копировать
     type NumberComposerDependencies = 
        class
            interface INumberComposerDependencies
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberComposerDependencies
Implements
    [INumberComposerDependencies](T_Tessa_Cards_Numbers_INumberComposerDependencies.htm)
##  __Конструкторы
[NumberComposerDependencies](M_Tessa_Cards_Numbers_NumberComposerDependencies__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[SequenceProviderDefault](P_Tessa_Cards_Numbers_NumberComposerDependencies_SequenceProviderDefault.htm)|
Объект [Tessa.Sequences.ISequenceProvider], предназначенный для
взаимодействием с последовательностями с выполнением транзакций.  
---|---  
[SequenceProviderWithoutTransaction](P_Tessa_Cards_Numbers_NumberComposerDependencies_SequenceProviderWithoutTransaction.htm)|
Объект [Tessa.Sequences.ISequenceProvider], предназначенный для
взаимодействием с последовательностями без выполнения транзакций.  
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
