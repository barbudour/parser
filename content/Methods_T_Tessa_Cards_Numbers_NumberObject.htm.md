# NumberObject - методы
##  __Методы
[CompareTo](M_Tessa_Cards_Numbers_NumberObject_CompareTo.htm)| Выполняет
сравнение текущего объекта с заданным.  
---|---  
[CreateEmpty](M_Tessa_Cards_Numbers_NumberObject_CreateEmpty.htm)|  Создаёт
объект [NumberObject](T_Tessa_Cards_Numbers_NumberObject.htm), описывающий
пустой номер.  
[Equals(INumberObject)](M_Tessa_Cards_Numbers_NumberObject_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_Numbers_NumberObject_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_Numbers_NumberObject_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsEmpty](M_Tessa_Cards_Numbers_NumberObject_IsEmpty.htm)|  Возвращает признак
того, что объект [Tessa.Cards.Numbers.INumberObject] представляет из себя
ссылку на отсутствующий (или ещё не известный) номер. Как правило, номер
считается пустым, если его строка полного номера равна null или пустой строке,
а также либо отсутствует числовой номер, либо имя последовательности равно
null или пустой строке. Т.о. пустой номер не является номером из
последовательности.  
[IsSequential()](M_Tessa_Cards_Numbers_NumberObject_IsSequential.htm)|
Возвращает признак того, что объект [Tessa.Cards.Numbers.INumberObject]
представляет из себя ссылку на номер из последовательности. Как правило, номер
считается взятым из последовательности, если его числовое представление, и имя
последовательности не равны null или пустой строке. Строка полного номера
может быть равна null или пустой строке. Т.о. пустой номер не является номером
из последовательности. Если номер не является номером из последовательности,
то его нельзя освободить, дерезервировать или выделить повторно.  
[IsSequential(Nullable<Int64>,
String)](M_Tessa_Cards_Numbers_NumberObject_IsSequential_1.htm)|  Возвращает
признак того, что номер, содержащий указанные значения в полях, является
номером из последовательности.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_Numbers_NumberObject_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_Numbers_NumberObject_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](M_Tessa_Cards_Numbers_NumberObject_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[RefreshFullNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_RefreshFullNumberAsync.htm)|
Обновляет поле с полным номером
[FullNumber](P_Tessa_Cards_Numbers_INumberObject_FullNumber.htm) для заданного
номера, если номер является номером последовательности, и возвращает объект
номера с такими же данными, но другим полным номером, или возвращает тот же
номер, если он не является номером последовательности.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_2.htm)|
Сохраняет объект с номером в заданном контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_1.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
