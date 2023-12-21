# NumberBuilder.GetDefaultSequenceName - метод
Возвращает имя последовательности, рекомендуемое для организации номеров
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static string GetDefaultSequenceName(
    	INumberContext context,
    	NumberTypeDescriptor numberType
    )
VB __Копировать
     Protected Shared Function GetDefaultSequenceName ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor
    ) As String
C++ __Копировать
     protected:
    static String^ GetDefaultSequenceName(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType
    )
F# __Копировать
     static member GetDefaultSequenceName : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor -> string 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера, для которого формируется имя последовательности.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя последовательности, рекомендуемое для организации номеров карточек.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
